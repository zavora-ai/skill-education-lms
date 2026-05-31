# Grade Report Template

Use this structure when presenting student grade summaries.

---

## 🎓 {student_name} — {course_name}

**Term:** {term} | **Instructor:** {instructor} | **Status:** {enrollment_status}

### Grade Summary

| Assessment | Weight | Score | Grade |
|------------|--------|-------|-------|
| {assessment_name} | {weight}% | {score}/{max_score} | {grade} |

**Overall Grade:** {overall_grade} ({overall_pct}%)

### Performance Indicators

| Metric | Value |
|--------|-------|
| Attendance | {attendance_pct}% |
| Assignments Submitted | {submitted}/{total_assignments} |
| Class Rank | {rank}/{class_size} |

{if overall_pct >= 90: "🌟 Excellent performance"}
{if overall_pct < 60: "⚠️ At risk — recommend academic support"}
{if attendance_pct < 75: "🚨 Low attendance — intervention needed"}

---

*Generated from mcp-education | {timestamp}*
