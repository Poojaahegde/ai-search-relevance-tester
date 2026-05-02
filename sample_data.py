"""
Sample query-result dataset for a SaaS project management tool.
Simulates realistic search evaluation scenarios with relevance labels.
Labels: 0=not relevant, 1=partially relevant, 2=relevant, 3=highly relevant
"""


def get_sample_data():
      return {
                "queries": [
                              "how to invite team members",
                              "billing settings",
                              "export project to CSV",
                              "task dependencies",
                              "notification preferences",
                              "how to create a project template",
                              "delete a task",
                              "integrate with Slack",
                              "due date filter",
                              "user permissions",
                ],
                "results": [
                              # Query: "how to invite team members"
                    [
                                      {"result_title": "Invite team members to your workspace", "result_content": "Learn how to invite team members and manage access in your workspace settings."},
                                      {"result_title": "User roles and permissions", "result_content": "Understand different user roles: admin, member, guest, and how to assign them."},
                                      {"result_title": "Managing your team", "result_content": "Add, remove, and manage team members from the People section in settings."},
                                      {"result_title": "Workspace settings overview", "result_content": "Configure your workspace name, logo, and general settings."},
                                      {"result_title": "Getting started guide", "result_content": "A complete guide to setting up your workspace for the first time."},
                    ],
                              # Query: "billing settings"
                              [
                                                {"result_title": "Billing & subscription", "result_content": "Manage your subscription plan, payment methods, and billing history."},
                                                {"result_title": "Upgrade your plan", "result_content": "Compare plans and upgrade to unlock advanced features."},
                                                {"result_title": "Account settings", "result_content": "Update your profile, password, and notification preferences."},
                                                {"result_title": "Team plan features", "result_content": "Explore what's included in the Team plan for growing organizations."},
                                                {"result_title": "Cancel subscription", "result_content": "Instructions for canceling your subscription and managing offboarding."},
                              ],
                              # Query: "export project to CSV"
                              [
                                                {"result_title": "Getting started guide", "result_content": "Introduction to the platform and how to create your first project."},
                                                {"result_title": "Project overview", "result_content": "See all your projects in one view with status, progress, and deadlines."},
                                                {"result_title": "Export and reporting", "result_content": "Export your project data to CSV, Excel, or PDF for external reporting."},
                                                {"result_title": "Integrations overview", "result_content": "Connect your tools: Slack, GitHub, Jira, and 50+ other integrations."},
                                                {"result_title": "Import projects from CSV", "result_content": "Import existing project data from a CSV file into the platform."},
                              ],
                              # Query: "task dependencies"
                              [
                                                {"result_title": "Task management basics", "result_content": "Create, assign, and track tasks across your projects."},
                                                {"result_title": "Adding dependencies between tasks", "result_content": "Set predecessor and successor relationships between tasks to manage sequencing."},
                                                {"result_title": "Gantt chart view", "result_content": "Visualize your project timeline with dependencies in Gantt view."},
                                                {"result_title": "Task status and labels", "result_content": "Use status labels to track task progress: To Do, In Progress, Done."},
                                                {"result_title": "Blocking and blocked-by relationships", "result_content": "Mark tasks as blocking others to surface critical path items."},
                              ],
                              # Query: "notification preferences"
                              [
                                                {"result_title": "Notification settings", "result_content": "Customize which events trigger notifications and how you receive them."},
                                                {"result_title": "Email digest settings", "result_content": "Choose between real-time, daily, or weekly email summaries."},
                                                {"result_title": "Account settings", "result_content": "Manage your account details, security, and preferences."},
                                                {"result_title": "Mobile push notifications", "result_content": "Configure push notifications for the mobile app."},
                                                {"result_title": "Slack notification integration", "result_content": "Receive task and project notifications directly in Slack."},
                              ],
                              # Query: "how to create a project template"
                              [
                                                {"result_title": "Project templates", "result_content": "Create reusable project templates to standardize workflows across your team."},
                                                {"result_title": "Template library", "result_content": "Browse pre-built templates for marketing, engineering, product, and more."},
                                                {"result_title": "Creating a new project", "result_content": "Start a project from scratch or choose from a template."},
                                                {"result_title": "Duplicate a project", "result_content": "Copy an existing project including all tasks and settings."},
                                                {"result_title": "Project settings", "result_content": "Configure project name, dates, members, and visibility."},
                              ],
                              # Query: "delete a task"
                              [
                                                {"result_title": "Managing tasks", "result_content": "Create, edit, assign, and delete tasks within your projects."},
                                                {"result_title": "Task actions: edit, archive, delete", "result_content": "Right-click on any task to access quick actions including delete."},
                                                {"result_title": "Archiving vs. deleting", "result_content": "Understand the difference between archiving a task (recoverable) and deleting (permanent)."},
                                                {"result_title": "Bulk task operations", "result_content": "Select multiple tasks and apply bulk actions including delete."},
                                                {"result_title": "Keyboard shortcuts", "result_content": "Speed up your workflow with keyboard shortcuts for common task actions."},
                              ],
                              # Query: "integrate with Slack"
                              [
                                                {"result_title": "Slack integration setup", "result_content": "Connect your workspace to Slack to receive notifications and manage tasks from Slack."},
                                                {"result_title": "Available integrations", "result_content": "Browse all available integrations including Slack, GitHub, Jira, and more."},
                                                {"result_title": "Slack slash commands", "result_content": "Use /task, /project, and /status commands directly in Slack."},
                                                {"result_title": "Integration settings", "result_content": "Manage which channels receive notifications and which events trigger them."},
                                                {"result_title": "Zapier integration", "result_content": "Connect to 5000+ apps through Zapier for automated workflows."},
                              ],
                              # Query: "due date filter"
                              [
                                                {"result_title": "Filtering and sorting tasks", "result_content": "Filter your task list by due date, assignee, status, priority, and more."},
                                                {"result_title": "Due date reminders", "result_content": "Set automatic reminders before task due dates via email or push notification."},
                                                {"result_title": "Calendar view", "result_content": "View all tasks with due dates in a calendar format by day, week, or month."},
                                                {"result_title": "Overdue task report", "result_content": "Quickly find all tasks past their due date in one view."},
                                                {"result_title": "Advanced filters", "result_content": "Combine multiple filters including due date ranges for complex queries."},
                              ],
                              # Query: "user permissions"
                              [
                                                {"result_title": "User roles and permissions", "result_content": "Manage what each user can see and do: admin, member, guest roles explained."},
                                                {"result_title": "Project-level access control", "result_content": "Set different permission levels per project for fine-grained access control."},
                                                {"result_title": "Invite team members", "result_content": "Add new members to your workspace and assign their initial role."},
                                                {"result_title": "Guest access", "result_content": "Invite external collaborators with limited access to specific projects only."},
                                                {"result_title": "Security settings", "result_content": "Configure SSO, 2FA, and session management for your workspace."},
                              ],
                ],
                "labels": [
                              [3, 2, 2, 1, 1],  # invite team members
                              [3, 2, 1, 1, 2],  # billing settings
                              [0, 1, 3, 0, 2],  # export to CSV — ranking failure: most relevant at pos 3
                              [1, 3, 2, 1, 2],  # task dependencies — partial failure: pos 2 most relevant
                              [3, 2, 1, 2, 1],  # notification preferences
                              [3, 2, 2, 1, 1],  # create project template
                              [2, 3, 2, 2, 1],  # delete a task
                              [3, 2, 2, 2, 1],  # integrate with Slack
                              [3, 2, 2, 2, 3],  # due date filter
                              [3, 2, 2, 2, 1],  # user permissions
                ],
      }
