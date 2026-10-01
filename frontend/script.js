const form = document.getElementById("employeeinput");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const payload = {
        first_name: form.first_name.value,
        last_name: form.last_name.value,
        age: Number(form.age.value),
        dept_id: Number(form.dept_id.value),
        role_id: Number(form.role_id.value)
    };

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/employeeinput",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            }
        );

        const data = await response.json();

        if (data.employee) {
            alert(data.message);

            form.reset();

            await loadEmployees();
        } else {
            alert(data.message);
        }

    } catch (error) {
        console.error("FULL ERROR:", error);
        alert("Network Error");
    }
});


async function loadEmployees() {
    try {
        const response = await fetch(
            "http://127.0.0.1:8000/employees"
        );

        const employees = await response.json();

        const tableBody = document.getElementById("Tablebody");

        tableBody.innerHTML = "";

        employees.forEach(emp => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${emp.id}</td>
                <td>${emp.first_name}</td>
                <td>${emp.last_name}</td>
                <td>${emp.age}</td>
                <td>${emp.dept_name}</td>
                <td>${emp.role_name}</td>
            `;

            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Error loading employees:", error);
    }
    
}

loadEmployees();


async function searchEmployee() {

    const employeeId = document.getElementById("searchId").value;

    if (!employeeId) {
        loadEmployees();
        return;
    }

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/employees/filter?id=${employeeId}`
        );

        const emp = await response.json();

        document.getElementById("editBtn").style.display = "inline-block";

        console.log(emp);

        const tableBody = document.getElementById("Tablebody");

        tableBody.innerHTML = "";

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${emp.id}</td>
            <td>${emp.first_name}</td>
            <td>${emp.last_name}</td>
            <td>${emp.age}</td>
            <td>${emp.dept_name}</td>
            <td>${emp.role_name}</td>
        `;

        tableBody.appendChild(row);

    } catch (error) {

        console.error(error);

        alert("Employee not found");

    }

}


async function showEditForm() {
    const row = document.querySelector("#Tablebody tr");

    if (!row) {
        alert("Please search for an employee first.");
        return;
    }

    const cells = row.querySelectorAll("td");
    const id = cells[0].textContent.trim();

    // Fill the basic details from the displayed row.
    document.getElementById("editId").value = id;
    document.getElementById("editFirstName").value =
        cells[1].textContent.trim();
    document.getElementById("editLastName").value =
        cells[2].textContent.trim();
    document.getElementById("editAge").value =
        cells[3].textContent.trim();

    // Use the department and role names as fallbacks.
    const departmentIds = {
        "engineering": "1",
        "hr": "2",
        "finance": "3",
        "data": "4"
    };

    const roleIds = {
        "backend developer": "1",
        "frontend developer": "2",
        "data analyst": "3",
        "manager": "4",
        "hr executive": "5"
    };

    const departmentName = cells[4].textContent.trim().toLowerCase();
    const roleName = cells[5].textContent.trim().toLowerCase();

    document.getElementById("editDepartment").value =
        departmentIds[departmentName] || "";

    document.getElementById("editRole").value =
        roleIds[roleName] || "";

    // Show the form immediately.
    document.getElementById("editSection").style.display = "block";

    // Fetch the employee record to get the actual foreign-key IDs.
    try {
        const response = await fetch(
            `http://127.0.0.1:8000/employees/filter?id=${id}`
        );

        if (!response.ok) {
            throw new Error("Could not load employee details");
        }

        const emp = await response.json();

        if (emp.dept_id != null) {
            document.getElementById("editDepartment").value =
                String(emp.dept_id);
        }

        if (emp.role_id != null) {
            document.getElementById("editRole").value =
                String(emp.role_id);
        }
    } catch (error) {
        console.error("Could not fetch employee IDs:", error);
    }

    document.getElementById("editSection").scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}

function closeEditForm() {
    document.getElementById("editSection").style.display = "none";
}

async function loadEmployeeForEdit(id) {
    try {
        const response = await fetch(
            `http://127.0.0.1:8000/employees/filter?id=${id}`
        );

        if (!response.ok) {
            throw new Error("Could not load employee details");
        }

        const emp = await response.json();

        document.getElementById("editDepartment").value = emp.dept_id;
        document.getElementById("editRole").value = emp.role_id;

    } catch (error) {
        console.error("Error loading employee for editing:", error);
        alert("Could not load department and role details.");
    }
}




document.getElementById("editForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("editId").value;

    const payload = {
        first_name: document.getElementById("editFirstName").value.trim(),
        last_name: document.getElementById("editLastName").value.trim(),
        age: Number(document.getElementById("editAge").value),
        dept_id: Number(document.getElementById("editDepartment").value),
        role_id: Number(document.getElementById("editRole").value)
    };

    console.log("Sending update:", { id, ...payload });

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/employees/filter?id=${id}`,
            {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            }
        );

        const data = await response.json();

        console.log("Update status:", response.status);
        console.log("Backend response:", data);

        if (!response.ok || data.message === "Employee not found") {
            throw new Error(
                data.detail || data.message || "Update failed"
            );
        }

        alert(data.message || "Employee updated successfully!");

        document.getElementById("editSection").style.display = "none";
        document.getElementById("searchId").value = "";

        // Fetch the latest employee records
        await loadEmployees();

    } catch (error) {
        console.error("Update failed:", error);
        alert("Update failed: " + error.message);
    }
});