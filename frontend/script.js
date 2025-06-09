async function addDonor() {
    const name = document.getElementById("name").value;
    const bloodType = document.getElementById("blood_type").value;
    const contactInfo = document.getElementById("contact_info").value;

    const response = await fetch("http://localhost:5000/add_donor", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            blood_type: bloodType,
            contact_info: contactInfo
        })
    });

    const result = await response.json();
    alert(result.message);
}

async function getDonors() {
    const response = await fetch("http://localhost:5000/donors");
    const donors = await response.json();

    const donorList = document.getElementById("donor_list");
    donorList.innerHTML = "";

    donors.forEach(donor => {
        const item = document.createElement("li");
        item.textContent = `Name: ${donor.name}, Blood Type: ${donor.blood_type}, Contact: ${donor.contact_info}`;
        donorList.appendChild(item);
    });
}

async function addRequest() {
    const bloodType = document.getElementById("req_blood_type").value;
    const quantity = document.getElementById("quantity").value;
    const requestorName = document.getElementById("requestor_name").value;
    const contactInfo = document.getElementById("req_contact_info").value;

    const response = await fetch("http://localhost:5000/add_request", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            blood_type: bloodType,
            quantity: quantity,
            requestor_name: requestorName,
            contact_info: contactInfo
        })
    });

    const result = await response.json();
    alert(result.message);
}

async function getRequests() {
    const response = await fetch("http://localhost:5000/blood_requests");
    const requests = await response.json();

    const requestList = document.getElementById("request_list");
    requestList.innerHTML = "";

    requests.forEach(req => {
        const item = document.createElement("li");
        item.textContent = `Blood Type: ${req.blood_type}, Quantity: ${req.quantity}, Requestor: ${req.requestor_name}, Contact: ${req.contact_info}`;
        requestList.appendChild(item);
    });
}
