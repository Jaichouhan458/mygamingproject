document.getElementById("signinForm").addEventListener("submit", function (event) {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === "" || password === "") {
      event.preventDefault(); // Prevent form submission
      alert("All fields are required!");
  }
});
