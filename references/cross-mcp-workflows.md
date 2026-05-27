# Education Cross-MCP Workflows

## Education + Email: Assignment Reminder
```
EDU: list_assignments(course_id, due_soon: true) → [{title: "HW3", due: "tomorrow"}]
EMAIL: send_email(to: class_list, subject: "Reminder: HW3 due tomorrow")
```

## Education + Slack: Announcement
```
EDU: post_announcement(course_id, title: "Midterm moved to March 5")
SLACK: send_message(channel: "#cs101", text: "📢 Midterm moved to March 5")
```
