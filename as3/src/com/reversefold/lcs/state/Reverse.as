package com.reversefold.lcs.state {
    import com.reversefold.lcs.LCSFSM;
    
    import flash.events.Event;

    public class Reverse extends LCSState {
		public function Reverse(lcs : LCSFSM) {
            super(lcs);
			lcs.idx_a = lcs.input_a.length;
			lcs.idx_b = lcs.input_b.length;
        }
		
		override public function next() : LCSState {
			if (lcs.match_matrix[lcs.idx_a][lcs.idx_b] == lcs.match_matrix[lcs.idx_a - 1][lcs.idx_b]) {
				lcs.idx_a -= 1;
				lcs.result_a.unshift(lcs.input_a[lcs.idx_a]);
				lcs.result_b.unshift(null);
				lcs.resultIndexes.unshift([lcs.idx_a, null]);
			} else if (lcs.match_matrix[lcs.idx_a][lcs.idx_b] == lcs.match_matrix[lcs.idx_a][lcs.idx_b - 1]) {
				lcs.idx_b -= 1;
				lcs.result_a.unshift(null);
				lcs.result_b.unshift(lcs.input_b[lcs.idx_b]);
				lcs.resultIndexes.unshift([null, lcs.idx_b]);
			} else {
				lcs.idx_a -= lcs.codon_length;
				lcs.idx_b -= lcs.codon_length;
				lcs.result_a.unshift.apply(lcs.result_a, lcs.input_a.slice(lcs.idx_a, lcs.idx_a + lcs.codon_length));
				lcs.result_b.unshift.apply(lcs.result_b, lcs.input_b.slice(lcs.idx_b, lcs.idx_b + lcs.codon_length));
				for (var i : uint = 0; i < lcs.codon_length; ++i) {
					lcs.resultIndexes.unshift([lcs.idx_a + i, lcs.idx_b + i]);
				}
			}
			
			lcs.dispatchEvent(new Event("resultAChanged"));
			lcs.dispatchEvent(new Event("resultBChanged"));
			lcs.dispatchEvent(new Event("resultIndexesChanged"));
			if (lcs.idx_a <= lcs.codon_length_less_1 || lcs.idx_b <= lcs.codon_length_less_1) {
				return new CleanupA(lcs);
			}
			return this;
		}
    }
}
