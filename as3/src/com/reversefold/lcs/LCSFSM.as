package com.reversefold.lcs {
	import com.reversefold.lcs.state.Forward;
	import com.reversefold.lcs.state.LCSState;
	
	import flash.events.Event;
	import flash.events.EventDispatcher;

    public class LCSFSM extends EventDispatcher {
		[Bindable]
		public var numberOfTicks : uint = 0;
		
		private var _result : Array;
		[Bindable(event="resultChanged")]
		public function get result() : Array {
			return _result;
		}
		
		private var _match_matrix : Array = [];
		[Bindable(event="matchMatrixChanged")]
		public function get match_matrix() : Array {
			return _match_matrix;
		}
		
		private var _matching_points : Array = [];
		[Bindable(event="matchingPointsChanged")]
		public function get matching_points() : Array {
			return _matching_points;
		}
		
		private var _input_a : Array;
		public function get input_a() : Array {
			return _input_a;
		}
		
		private var _input_b : Array;
		public function get input_b() : Array {
			return _input_b;
		}
		
		private var _codon_length : uint;
		public function get codon_length() : uint {
			return _codon_length;
		}
		
		private var _codon_length_less_1 : uint;
		public function get codon_length_less_1() : uint {
			return _codon_length_less_1;
		}
		
		private var _state : LCSState;
		[Bindable(event="stateChanged")]
		public function get state() : LCSState {
			return _state;
		}
		
		private var _display_matrix : Array = [];
		[Bindable(event="displayMatrixChanged")]
		public function get display_matrix() : Array {
			return _display_matrix;
		}
		
		private var _result_a : Array = [];
		[Bindable(event="resultAChanged")]
		public function get result_a() : Array {
			return _result_a;
		}
		
		private var _result_b : Array = [];
		[Bindable(event="resultBChanged")]
		public function get result_b() : Array {
			return _result_b;
		}
		
		private var _resultIndexes : Array = [];
		[Bindable(event="resultIndexesChanged")]
		public function get resultIndexes() : Array {
			return _resultIndexes;
		}
		
		[Bindable]
		public var idx_a : uint;
		[Bindable]
		public var idx_b : uint;
		
        public function LCSFSM(input_a : Array, input_b : Array, codon_length : uint) : void {
			_input_a = input_a;
			_input_b = input_b;
			trace(_input_a);
			trace(_input_b);
			this._codon_length = codon_length;
			this._codon_length_less_1 = codon_length - 1;
			for (var idx_a : uint = 0; idx_a < _input_a.length + 1; ++idx_a) {
				_match_matrix.push([]);
				_matching_points.push([]);
				for (var idx_b : uint = 0; idx_b < _input_b.length + 1; ++idx_b) {
					_match_matrix[idx_a].push(0);
					_matching_points[idx_a].push('');
				}
			}
			_state = new Forward(this);
		}
		
		public function next() : Boolean {
			if (_state == null) {
				throw new Error("Finished (StopIteration)");
			}
			++numberOfTicks;
			if (!_state.next()) {
				_state = _state.nextState();
				dispatchEvent(new Event("stateChanged"));
			}
			if (state == null) {
				trace(result_a);
				trace(result_b);
				var p_a : Array = result_a.concat();
				var p_b : Array = result_b.concat();
				for (idx_a = 0; idx_a < p_a.length; ++idx_a) {
					if (p_a[idx_a] == null) {
						p_a[idx_a] = " ";
					}
				}
				for (idx_b = 0; idx_b < p_b.length; ++idx_b) {
					if (p_b[idx_b] == null) {
						p_b[idx_b] = " ";
					}
				}
				trace("'" + p_a.join("") + "'");
				trace("'" + p_b.join("") + "'");
				_result = [result_a, result_b, _match_matrix[_input_a.length][_input_b.length]];
				return false;
			} else {
				return true;
			}
		}
		
		public function run() : void {
			while (next()) {}
		}
    }
}
