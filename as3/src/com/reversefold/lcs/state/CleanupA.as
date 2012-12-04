package com.reversefold.lcs.state {
	import com.reversefold.lcs.LCSFSM;
	
	import flash.events.Event;
	
	public class CleanupA extends LCSState {
		public function CleanupA(lcs : LCSFSM) {
			super(lcs);
		}
		
		override public function next() : Boolean {
			if (lcs.idx_a > 0) {
				lcs.idx_a -= 1;
				lcs.result_a.unshift(lcs.input_a[lcs.idx_a]);
				lcs.result_b.unshift(null);
				lcs.resultIndexes.unshift([lcs.idx_a, null]);
				lcs.dispatchEvent(new Event("resultAChanged"));
				lcs.dispatchEvent(new Event("resultBChanged"));
				lcs.dispatchEvent(new Event("resultIndexesChanged"));
				return true;
			}
			_done = true;
			return false;
		}
		
		override public function nextState() : LCSState {
			if (!done) {
				throw new Error("Not done");
			}
			return new CleanupB(lcs);
		}
	}
}