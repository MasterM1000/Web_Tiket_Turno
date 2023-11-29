function consultarTicket() {
    // Get the CURP input value
    const curpInput = document.querySelector("input[name='CURP']");
    const curp = curpInput.value;

    // Make an AJAX request to fetch ticket data
    fetch("/consultar_ticket", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ curp: curp }),
    })
    .then((response) => response.json())
    .then((ticketData) => {
        // Populate the form fields with ticket data
        if (ticketData) {
            const nombreInput = document.querySelector("input[name='nombre']");
            nombreInput.value = ticketData.nombre;

            const apePaterInput = document.querySelector("input[name='Apater']");
            apePaterInput.value = ticketData.apePater;

            const apeMaterInput = document.querySelector("input[name='Amater']");
            apeMaterInput.value = ticketData.apeMater;

            // ... Repeat for other form fields

            // Prevent the form from submitting
            document.querySelector("form").submit = false;
        } else {
            // Handle the case where no ticket is found
            alert("No se encontró ningún ticket con ese CURP");
        }
    });
}
