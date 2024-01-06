#### Procedural Approach (hitting the ceiling)

```cpp
#include <iostream>
#include <string>
#include <vector>

struct Employee {
    std::string name;
    int employeeID;
    std::string department;
};

struct Task {
    std::string name;
    int progress;
    Employee assignedEmployee;
};

struct Project {
    std::string name;
    std::vector<std::string> resources;
    std::vector<Task> tasks;
};

void assignTask(const Project& project, const std::string& taskName, const Employee& employee) {
    std::cout << "Assigning task '" << taskName << "' in project " << project.name << " to employee " << employee.name << " (ID: " << employee.employeeID << ") from the " << employee.department << " department.\n";
}

void trackProgress(const Task& task) {
    std::cout << "Tracking progress of task '" << task.name << "': " << task.progress << "%.\n";
}

void manageResources(const Project& project) {
    std::cout << "Managing resources for project " << project.name << ": ";
    for (const auto& resource : project.resources) {
        std::cout << resource << ", ";
    }
    std::cout << "\n";
}

void stressTest(int numProjects, int numEmployees, int numTasks) {
    // Limitation fixed: Improved modularity and scalability in procedural approach
    std::vector<Project> projects;

    for (int i = 0; i < numProjects; ++i) {
        Project project;
        project.name = "Project" + std::to_string(i);
        project.resources = {"Resource1", "Resource2", "Resource3"};
        for (int j = 0; j < numEmployees; ++j) {
            Employee employee{"Employee" + std::to_string(j), 1000 + j, "Department" + std::to_string(j % 3)};
            project.tasks.push_back({"Task" + std::to_string(j), 0, employee});
        }
        projects.push_back(project);
    }

    // Limitation fixed: Improved clarity and readability in managing multiple projects
    for (const auto& project : projects) {
        std::cout << "Project: " << project.name << "\n";
        manageResources(project);
        for (const auto& task : project.tasks) {
            assignTask(project, task.name, task.assignedEmployee);
            trackProgress(task);
        }
    }
}

int main() {
    // Example using procedural approach with limitations demonstrated
    Project enterpriseSoftware;
    enterpriseSoftware.name = "Enterprise Software";
    enterpriseSoftware.resources = {"Developer1", "Developer2", "QA Engineer", "Project Manager", "UI/UX Designer", "DevOps Engineer"};

    std::vector<Employee> employees = {
        {"John Doe", 1001, "Development"},
        {"Alice Johnson", 1002, "Development"},
        {"Bob Smith", 1003, "QA"},
        {"Eva Rodriguez", 1004, "Project Management"},
        {"Michael Brown", 1005, "UI/UX Design"},
        {"Sophia Kim", 1006, "Development"},
        {"David Wilson", 1007, "DevOps"},
        {"Emma Lee", 1008, "Development"},
        {"Daniel Garcia", 1009, "QA"},
        {"Olivia Martinez", 1010, "Project Management"}
    };

    std::vector<Task> projectTasks = {
        {"Task1", 0, employees[0]},
        {"Task2", 0, employees[1]},
        {"Task3", 0, employees[2]},
        {"Task4", 0, employees[3]},
        {"Task5", 0, employees[4]},
        {"Task6", 0, employees[5]},
        {"Task7", 0, employees[6]},
        {"Task8", 0, employees[7]},
        {"Task9", 0, employees[8]},
        {"Task10", 0, employees[9]}
    };

    for (auto& task : projectTasks) {
        assignTask(enterpriseSoftware, task.name, task.assignedEmployee);
        trackProgress(task);
        enterpriseSoftware.tasks.push_back(task);
    }

    manageResources(enterpriseSoftware);

    // Limitation: Difficulty in managing multiple projects in a scalable manner
    stressTest(5, 10, 15);

    return 0;
}
```

#### OOP Approach (Fixed)

```cpp
#include <iostream>
#include <string>
#include <vector>

class Employee {
public:
    std::string name;
    int employeeID;
    std::string department;

    Employee(const std::string& empName, int empID, const std::string& empDepartment)
        : name(empName), employeeID(empID), department(empDepartment) {}
};

class Task {
public:
    std::string name;
    int progress;
    Employee assignedEmployee;

    Task(const std::string& taskName, const Employee& emp)
        : name(taskName), progress(0), assignedEmployee(emp) {}

    void trackProgress() const {
        std::cout << "Tracking progress of task '" << name << "': " << progress << "%.\n";
    }
};

class Project {
public:
    std::string name;
    std::vector<std::string> resources;
    std::vector<Task> tasks;

    Project(const std::string& projectName, const std::vector<std::string>& projectResources)
        : name(projectName), resources(projectResources) {}

    void assignTask(const Task& task) const {
        std::cout << "Assigning task '" << task.name << "' in project " << name << " to employee " << task.assignedEmployee.name << " (ID: " << task.assignedEmployee.employeeID << ") from the " << task.assignedEmployee.department << " department.\n";
    }

    void manageResources() const {
        std::cout << "Managing resources for project " << name << ": ";
        for (const auto& resource : resources) {
            std::cout << resource << ", ";
        }
        std::cout << "\n";
    }
};

void stressTest(int numProjects, int numEmployees, int numTasks) {
    // Improved: Example using OOP approach with better scalability and modularity
    std::vector<Project> projects;

    for (int i = 0; i < numProjects; ++i) {
        Project project("Project" + std::to_string(i), {"Resource1", "Resource2", "Resource3"});
        for (int j = 0; j < numEmployees; ++j) {
            Employee employee{"Employee" + std::to_string(j), 1000 + j, "Department" + std::to_string(j % 3)};
            project.resources.push_back(employee.name);
            for (int k = 0; k < numTasks; ++k) {
                Task task("Task" + std::to_string(k), employee);
                project.tasks.push_back(task);
            }
        }
        projects.push_back(project);
    }

    // Improved: Managing multiple projects in a scalable manner
    for (const auto& project : projects) {
        std::cout << "Project: " << project.name << "\n";
        project.manageResources();
        for (const auto& task : project.tasks) {
           

 project.assignTask(task);
            task.trackProgress();
        }
    }
}

int main() {
    // Example using OOP approach with an even more complex and demanding scenario
    Project enterpriseSoftware("Enterprise Software", {"Developer1", "Developer2", "QA Engineer", "Project Manager", "UI/UX Designer", "DevOps Engineer"});

    std::vector<Employee> employees = {
        {"John Doe", 1001, "Development"},
        {"Alice Johnson", 1002, "Development"},
        {"Bob Smith", 1003, "QA"},
        {"Eva Rodriguez", 1004, "Project Management"},
        {"Michael Brown", 1005, "UI/UX Design"},
        {"Sophia Kim", 1006, "Development"},
        {"David Wilson", 1007, "DevOps"},
        {"Emma Lee", 1008, "Development"},
        {"Daniel Garcia", 1009, "QA"},
        {"Olivia Martinez", 1010, "Project Management"}
    };

    std::vector<Task> projectTasks = {
        {"Task1", 0, employees[0]},
        {"Task2", 0, employees[1]},
        {"Task3", 0, employees[2]},
        {"Task4", 0, employees[3]},
        {"Task5", 0, employees[4]},
        {"Task6", 0, employees[5]},
        {"Task7", 0, employees[6]},
        {"Task8", 0, employees[7]},
        {"Task9", 0, employees[8]},
        {"Task10", 0, employees[9]}
    };

    for (auto& task : projectTasks) {
        enterpriseSoftware.assignTask(task);
        task.trackProgress();
        enterpriseSoftware.tasks.push_back(task);
    }

    enterpriseSoftware.manageResources();

    // Limitation fixed: Managing multiple projects in a scalable manner
    stressTest(5, 10, 15);

    return 0;
}
```
## Avoiding nested loops

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

struct Employee {
    std::string name;
    int employeeID;
    std::string department;

    Employee(const std::string& empName, int empID, const std::string& empDepartment)
        : name(empName), employeeID(empID), department(empDepartment) {}
};

struct Task {
    std::string name;
    int progress;
    Employee assignedEmployee;

    Task(const std::string& taskName, const Employee& emp)
        : name(taskName), progress(0), assignedEmployee(emp) {}

    void trackProgress() const {
        std::cout << "Tracking progress of task '" << name << "': " << progress << "%.\n";
    }
};

struct Project {
    std::string name;
    std::vector<std::string> resources;
    std::vector<Task> tasks;

    Project(const std::string& projectName, const std::vector<std::string>& projectResources)
        : name(projectName), resources(projectResources) {}

    void assignTask(const Task& task) const {
        std::cout << "Assigning task '" << task.name << "' in project " << name << " to employee " << task.assignedEmployee.name << " (ID: " << task.assignedEmployee.employeeID << ") from the " << task.assignedEmployee.department << " department.\n";
    }

    void manageResources() const {
        std::cout << "Managing resources for project " << name << ": ";
        for (const auto& resource : resources) {
            std::cout << resource << ", ";
        }
        std::cout << "\n";
    }
};

template <typename T>
void forEach(const std::vector<T>& items, const std::function<void(const T&)>& action) {
    std::for_each(items.begin(), items.end(), action);
}

template <typename T, typename Predicate>
std::vector<T> filter(const std::vector<T>& items, Predicate predicate) {
    std::vector<T> result;
    std::copy_if(items.begin(), items.end(), std::back_inserter(result), predicate);
    return result;
}

template <typename T, typename Mapper>
auto map(const std::vector<T>& items, Mapper mapper) -> std::vector<decltype(mapper(std::declval<T>()))> {
    std::vector<decltype(mapper(std::declval<T>()))> result;
    std::transform(items.begin(), items.end(), std::back_inserter(result), mapper);
    return result;
}

void stressTest(int numProjects, int numEmployees, int numTasks) {
    // Improved: Example using functional programming style
    std::vector<Project> projects;

    // Generate projects
    forEach(std::vector<int>(numProjects), [&](int i) {
        projects.emplace_back("Project" + std::to_string(i), {"Resource1", "Resource2", "Resource3"});
    });

    // Generate employees and tasks for each project
    forEach(projects, [&](const Project& project) {
        auto employees = map(std::vector<int>(numEmployees), [&](int j) {
            return Employee{"Employee" + std::to_string(j), 1000 + j, "Department" + std::to_string(j % 3)};
        });

        project.resources = map(employees, [](const Employee& emp) { return emp.name; });

        forEach(employees, [&](const Employee& employee) {
            auto tasks = map(std::vector<int>(numTasks), [&](int k) {
                return Task{"Task" + std::to_string(k), employee};
            });

            project.tasks.insert(project.tasks.end(), tasks.begin(), tasks.end());
        });
    });

    // Improved: Managing multiple projects in a scalable manner
    forEach(projects, [&](const Project& project) {
        std::cout << "Project: " << project.name << "\n";
        project.manageResources();

        forEach(project.tasks, [&](const Task& task) {
            project.assignTask(task);
            task.trackProgress();
        });
    });
}

int main() {
    // Example using functional programming style
    Project enterpriseSoftware("Enterprise Software", {"Developer1", "Developer2", "QA Engineer", "Project Manager", "UI/UX Designer", "DevOps Engineer"});

    auto employees = map(std::vector<int>(10), [](int i) {
        return Employee{"Employee" + std::to_string(i), 1001 + i, "Department" + std::to_string(i % 3)};
    });

    auto projectTasks = map(std::vector<int>(10), [&](int i) {
        return Task{"Task" + std::to_string(i), employees[i]};
    });

    forEach(projectTasks, [&](const Task& task) {
        enterpriseSoftware.assignTask(task);
        task.trackProgress();
        enterpriseSoftware.tasks.push_back(task);
    });

    enterpriseSoftware.manageResources();

    // Improved: Managing multiple projects in a scalable manner
    stressTest(5, 10, 15);

    return 0;
}
```
