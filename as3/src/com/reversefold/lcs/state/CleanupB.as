package com.reversefold.lcs.state {
    import com.reversefold.lcs.LCSFSM;
    
    import flash.events.Event;

    public class CleanupB extends LCSState {
        public function CleanupB(lcs : LCSFSM) {
            super(lcs);
        }
		
		override public function next() : Boolean {
			if (lcs.idx_b > 0) {
				lcs.idx_b -= 1;
				lcs.result_a.unshift(null);
				lcs.result_b.unshift(lcs.input_b[lcs.idx_b]);
				lcs.resultIndexes.unshift([null, lcs.idx_b]);
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
			return null;
		}
	}
}
