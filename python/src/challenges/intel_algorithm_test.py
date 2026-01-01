import pytest
from intel_algorithm import max_tasks
import sys, os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def test_max_tasks():
    # Basic mixed scenario: some tasks fit, some need to be dropped
    # Ensures the algorithm correctly removes the longest task when necessary
    assert max_tasks([(3,7),(1,2),(2,5),(4,6)]) == 3

    # All tasks fit comfortably within deadlines
    # Verifies that the algorithm accepts all tasks when possible
    assert max_tasks([(1,10),(2,12),(3,15)]) == 3

    # No tasks can be scheduled due to extremely tight deadlines
    # Tests the algorithm handles cases where zero tasks are possible
    assert max_tasks([(10,1),(5,2),(7,3)]) == 0

    # Multiple tasks with same deadline, requiring selection of optimal subset
    # Ensures the algorithm chooses tasks that maximize count, not just earliest duration
    assert max_tasks([(3,5),(2,5),(1,5)]) == 2

    # Single task scenario
    # Verifies the algorithm correctly handles minimal input
    assert max_tasks([(2,3)]) == 1

    # Increasing deadlines with decreasing durations create a tight cumulative constraint 
    # that tests whether the algorithm makes globally optimal scheduling choices.
    assert max_tasks([(5, 5),(4, 6),(3, 7),(2, 8)]) == 2

if __name__ == "__main__":
    pytest.main([__file__])
