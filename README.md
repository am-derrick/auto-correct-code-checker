# auto-correct-code-checker

This repository contains code for a code checker in python that can be integrated in an LMS.

- **Implementation 1:** - involves comparing the learner code against the rubric code so it matches.
  This implementation is inefficient as it only assumes one way of solving coding problems which in a real world case isn't true.
  It also wouldn't take to account the multiple coding languages one might use to solve the problem.

- **Implementation 2:** - involves comparing the learner code output against the rubric output.
  This method is more efficient as it measures only test cases.

  All these implementations involve using the GitHub API to get the learner code from a stated repo and then compare against the rubric.

