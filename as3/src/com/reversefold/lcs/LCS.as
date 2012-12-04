package com.reversefold.lcs {
	public class LCS {
		public static function print_table(arr : Array) : void {
			var r : String = "";
			var m : uint = 0;
			for each (var row : Array in arr) {
				for each (var o : * in row) {
					m = Math.max(m, new String(o).length);
				}
			}
			for each (row in arr) {
				for each (o in row) {
					var s : String = String(o);
					while (s.length < m) {
						s = " " + s;
					}
					r += s + " ";
				}
				r += "\n";
			}
			trace(r);
		}
		
		public static function arrays_equal(a : Array, b : Array, valuesEqual : Function) : Boolean {
			if (a.length != b.length) {
				return false;
			}
			for (var i : uint = 0; i < a.length; ++i) {
				if (!valuesEqual(a[i], b[i])) {
					return false;
				}
			}
			return true;
		}
		
		public static function values_equal(a : *, b : *) : Boolean {
			return a == b;
		}
		
		public static function lcs(input_a : Array, input_b : Array, codon_length : uint) : Array {
			trace(input_a);
			trace(input_b);
			var match_matrix : Array = [];
			var matching_points : Array = [];
			var x : uint;
			var y : uint;
			for (x = 0; x < input_a.length + 1; ++x) {
				match_matrix.push([]);
				matching_points.push([]);
				for (y = 0; y < input_b.length + 1; ++y) {
					match_matrix[x].push(0);
					matching_points[x].push('');
				}
			}
			var codon_length_less_1 : uint = codon_length - 1;
			for (x = codon_length - 1; x < input_a.length; ++x) {
				for (y = codon_length - 1; y < input_b.length; ++y) {
					match_matrix[x + 1][y + 1] = Math.max(
						((arrays_equal(
							input_a.slice(x - codon_length_less_1, x + 1),
							input_b.slice(y - codon_length_less_1, y + 1),
							values_equal)
							? 1 : 0)
							+ match_matrix[x - codon_length_less_1][y - codon_length_less_1]),
						
						match_matrix[x][y + 1],
						match_matrix[x + 1][y])
					if (match_matrix[x + 1][y + 1] != match_matrix[x][y + 1] && match_matrix[x + 1][y + 1] != match_matrix[x + 1][y]) {
						matching_points[x + 1][y + 1] = 'x';
					}
				}
			}
			
			var display_matrix : Array;
			display_matrix = match_matrix.concat(); //clone
			var i : uint;
			for (i = 0; i < display_matrix.length; ++i) {
				display_matrix[i] = display_matrix[i].concat(); //clone
			}
			display_matrix[0] = input_b.concat();
			display_matrix[0].unshift('');
			matching_points[0] = display_matrix[0].concat();
			for (x = 0; x < input_a.length; ++x) {
				display_matrix[x + 1][0] = input_a[x];
				matching_points[x + 1][0] = input_a[x];
			}
			print_table(display_matrix);
			print_table(matching_points);
			
			x = input_a.length;
			y = input_b.length;
			var result_a : Array;
			var result_b : Array;
			result_a = [];
			result_b = [];
			
			while (x > codon_length_less_1 && y > codon_length_less_1) {
				if (match_matrix[x][y] == match_matrix[x - 1][y]) {
					x -= 1;
					result_a.push(input_a[x]);
					result_b.push(null);
				} else if (match_matrix[x][y] == match_matrix[x][y - 1]) {
					y -= 1;
					result_a.push(null);
					result_b.push(input_b[y]);
				} else {
					x -= codon_length;
					y -= codon_length;
					result_a = result_a.concat(input_a.slice(x, x + codon_length).reverse());
					result_b = result_b.concat(input_b.slice(y, y + codon_length).reverse());
				}
			}
			while (x > 0) {
				x -= 1;
				result_a.push(input_a[x]);
				result_b.push(null);
			}
			while (y > 0) {
				y -= 1;
				result_a.push(null);
				result_b.push(input_b[y]);
			}
			result_a.reverse();
			result_b.reverse();
			trace(result_a);
			trace(result_b);
			var p_a : Array = result_a.concat();
			var p_b : Array = result_b.concat();
			for (x = 0; x < p_a.length; ++x) {
				if (p_a[x] == null) {
					p_a[x] = " ";
				}
			}
			for (y = 0; y < p_b.length; ++y) {
				if (p_b[y] == null) {
					p_b[y] = " ";
				}
			}
			trace("'" + p_a.join("") + "'");
			trace("'" + p_b.join("") + "'");
			return [result_a, result_b, match_matrix[input_a.length][input_b.length]];
		}
	}
}
