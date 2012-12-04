package com.reversefold.lcs.state {
	import com.reversefold.lcs.LCS;
	import com.reversefold.lcs.LCSFSM;
	
	import flash.events.Event;

    public class Forward extends LCSState {
		public function Forward(lcs : LCSFSM) {
			super(lcs);
			lcs.idx_a = lcs.codon_length - 1;
			lcs.idx_b = lcs.codon_length - 1;
        }
		
		override public function next() : LCSState {
			lcs.match_matrix[lcs.idx_a + 1][lcs.idx_b + 1] = Math.max(
				((LCS.arrays_equal(
					lcs.input_a.slice(lcs.idx_a - lcs.codon_length_less_1, lcs.idx_a + 1),
					lcs.input_b.slice(lcs.idx_b - lcs.codon_length_less_1, lcs.idx_b + 1),
					LCS.values_equal)
					? 1 : 0)
					+ lcs.match_matrix[lcs.idx_a - lcs.codon_length_less_1][lcs.idx_b - lcs.codon_length_less_1]),
				
				lcs.match_matrix[lcs.idx_a][lcs.idx_b + 1],
				lcs.match_matrix[lcs.idx_a + 1][lcs.idx_b])
			if (lcs.match_matrix[lcs.idx_a + 1][lcs.idx_b + 1] != lcs.match_matrix[lcs.idx_a][lcs.idx_b + 1]
				&& lcs.match_matrix[lcs.idx_a + 1][lcs.idx_b + 1] != lcs.match_matrix[lcs.idx_a + 1][lcs.idx_b]
			) {
				lcs.matching_points[lcs.idx_a + 1][lcs.idx_b + 1] = 'x';
			}
			
			++lcs.idx_b;
			if (lcs.idx_b == lcs.input_b.length) {
				++lcs.idx_a;
				if (lcs.idx_a == lcs.input_a.length) {
					lcs.display_matrix.splice.apply(lcs.display_matrix, [0, 0].concat(lcs.match_matrix)); 
					var i : uint;
					for (i = 0; i < lcs.display_matrix.length; ++i) {
						lcs.display_matrix[i] = lcs.display_matrix[i].concat(); //clone
					}
					lcs.display_matrix[0] = lcs.input_b.concat();
					lcs.display_matrix[0].unshift('');
					lcs.matching_points[0] = lcs.display_matrix[0].concat();
					for (lcs.idx_a = 0; lcs.idx_a < lcs.input_a.length; ++lcs.idx_a) {
						lcs.display_matrix[lcs.idx_a + 1][0] = lcs.input_a[lcs.idx_a];
						lcs.matching_points[lcs.idx_a + 1][0] = lcs.input_a[lcs.idx_a];
					}
					LCS.print_table(lcs.display_matrix);
					LCS.print_table(lcs.matching_points);
					lcs.dispatchEvent(new Event("matchMatrixChanged"));
					lcs.dispatchEvent(new Event("matchingPointsChanged"));
					return new Reverse(lcs);
				} else {
					lcs.idx_b = lcs.codon_length - 1;
				}
			}
			lcs.dispatchEvent(new Event("matchMatrixChanged"));
			return this;
		}
    }
}
