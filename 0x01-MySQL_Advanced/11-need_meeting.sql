-- lists all students that have score under 80 and no last_meeting or more than 1 month.

CREATE VIEW need_meeting AS SELECT students.name
FROM students WHERE students.score < 80 and
last_meeting IS NULL OR DATEDIFF(NOW(), last_meeting > 30)
