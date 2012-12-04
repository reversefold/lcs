package com.reversefold.lcs.state {
	import com.reversefold.lcs.LCSFSM;
	
	import flash.events.EventDispatcher;

    public class LCSState extends EventDispatcher {
		protected var lcs : LCSFSM;
		
        public function LCSState(lcs : LCSFSM) {
			this.lcs = lcs;
        }
		
		public function next() : LCSState {
			throw new Error("Implement me!");
		}
    }
}
