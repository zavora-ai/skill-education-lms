# Education Examples

## Example 1: "Create a homework assignment"
```
create_assignment(course_id: "CS101", title: "Week 3: Data Structures", description: "Implement a binary search tree...", due_date: "2025-02-07", points: 100)
```
Response: "✅ Assignment created: Week 3: Data Structures (100 pts, due Feb 7)"

## Example 2: "Grade the latest submissions"
```
get_submissions(assignment_id: "hw3") → [{student: "Alice", file: "bst.py"}, {student: "Bob", file: "bst.py"}]
grade_submission(id: "sub_alice", score: 92, feedback: "Excellent implementation. Consider adding balancing for bonus.")
```
Response: "Graded Alice: 92/100. Feedback provided."
