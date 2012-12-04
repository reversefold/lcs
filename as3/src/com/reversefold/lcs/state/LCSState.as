package com.reversefold.lcs.state {
	import com.reversefold.lcs.LCSFSM;

    public class LCSState {
		protected var lcs : LCSFSM;
		protected var _done : Boolean = false;
		
        public function LCSState(lcs : LCSFSM) {
			this.lcs = lcs;
        }
		
		public function get done() : Boolean {
			return _done;
		}
		
		public function nextState() : LCSState {
			throw new Error("Implement me!");
		}
		
		public function next() : Boolean {
			throw new Error("Implement me!");
		}
    }
}
