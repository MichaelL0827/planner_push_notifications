USE `todo`;

-- Insert Users
INSERT INTO `User` (`Username`, `Firstname`, `Lastname`, `Password`) VALUES
('john_doe', 'John', 'Doe', 'hashedpassword1'),
('jane_smith', 'Jane', 'Smith', 'hashedpassword2'),
('mike_ross', 'Mike', 'Ross', 'hashedpassword3'),
('alice_johnson', 'Alice', 'Johnson', 'hashedpassword4');

-- Insert Tasks (creator gets write access = 1)
INSERT INTO `Task` (`Name`, `Description`, `UserId`) VALUES
('Project Setup', 'Set up the project structure and dependencies', 1),  
('Design Database', 'Create ERD and database schema', 2),  
('Develop API', 'Build RESTful API for tasks', 3),  
('Frontend Development', 'Build UI components with Vue.js', 4);  

-- Insert Todos under tasks
INSERT INTO `Todo` (`Name`, `Description`, `Completed`, `Start`, `End`, `TaskId`) VALUES
('Initialize Git', 'Create a GitHub repository and push initial code', 1, '2025-02-15 08:00:00', '2025-02-15 09:00:00', 1),
('Create Database Schema', 'Write SQL scripts to create tables', 0, '2025-02-16 10:00:00', '2025-02-16 12:00:00', 2),
('Implement Authentication', 'Develop login and registration API', 0, '2025-02-17 14:00:00', '2025-02-17 18:00:00', 3),
('Design UI Components', 'Work on the login and dashboard UI using Vue.js', 0, '2025-02-18 09:00:00', '2025-02-18 12:00:00', 4);
