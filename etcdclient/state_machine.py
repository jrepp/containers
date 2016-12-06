
class StateMachine(object):
    def __init__(self, context={}, transition_map={}):
        self.current_state = None
        self.next_state = None
        self.transition_map = transition_map
        self.context = context

    def update(self):
        if self.next_state:
            self.current_state = self.next_state
            self.next_state = None

        if self.current_state:
            self.current_state(self.context)
    
    def signal(self, signal):
        signal_map = self.transition_map.get(self.current_state)
        to_state = None
        if signal_map is not None:
            to_state = signal_map.get(signal_map)
            
        if to_state is not None:
            self.next_state = to_state
            print 'sm[{0}] transition {1} -> {2} with: {3}'.format(
                self.name, self.current_state, self.next_state, signal)


    def add_transition(self, from_state, to_state, signal):
        signal_map = self.transition_map.get(from_state)
        if not signal_map:
            signal_map = { signal: to_state }
        else:
            signal_map.update( { signal: to_state } )
        self.set_transitions(from_state, signal_map)
       

    def set_transitions(self, from_state, signal_map):
        self.transition_map[from_state] = signal_map


