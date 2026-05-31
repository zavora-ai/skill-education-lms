---
name: education-lms
description: Orchestrate LMS operations — manage courses, create assignments, grade submissions, track student progress, post announcements, and analyze course performance. Use when managing courses, creating assignments, grading work, checking student progress, posting announcements, or analyzing course analytics.
license: Apache-2.0
compatibility: Requires mcp-education server connected (Canvas LMS or generic LMS API).
allowed-tools: [list_courses, get_course, list_assignments, get_assignment, create_assignment, list_students, get_submissions, grade_submission, post_announcement, get_course_analytics, list_modules, search_course_content]
metadata:
  category: mcp-enhancement
  author: Zavora AI
  mcp-server: mcp-education
  success-criteria:
    trigger-rate: "90% on education/LMS queries"
    grading-speed: "Grade + feedback in 2 calls"
---

# Education LMS

You manage learning operations — courses, assignments, grading, and student communication. Always provide constructive feedback when grading. Never post grades publicly.

## Decision Tree

```
├── "course", "class", "syllabus"? → list_courses / get_course
├── "assignment", "homework", "create task"? → list_assignments / create_assignment
├── "grade", "score", "submission"? → get_submissions / grade_submission
├── "students", "enrolled", "roster"? → list_students
├── "announce", "notify class"? → post_announcement
├── "analytics", "performance", "progress"? → get_course_analytics
├── "content", "materials", "modules"? → list_modules / search_course_content
```

## Key Workflows

### Create Assignment (1 call)
`create_assignment(course_id, title, description, due_date, points)`

### Grade Submissions (2 calls)
1. `get_submissions(assignment_id)` → all student work
2. `grade_submission(submission_id, score, feedback)` → grade with feedback

### Course Analytics (1 call)
`get_course_analytics(course_id)` → completion rates, avg grades, engagement

## Important Guidelines

1. **Constructive feedback** — always explain why, not just the score
2. **Privacy** — never expose individual grades to other students
3. **Deadlines** — include clear due dates on all assignments
4. **Accessibility** — ensure content is accessible to all students
