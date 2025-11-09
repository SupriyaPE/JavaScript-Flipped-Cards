const schoolData = `
{
  "schoolName": "Green Valley High School",
  "location": "Bangalore, India",
  "establishedYear": 1995,
  "teachers": [
    { "id": 1, "name": "Mrs. Priya Sharma", "subject": "Math", "experience": 10 },
    { "id": 2, "name": "Mr. Arjun Reddy", "subject": "Science", "experience": 8 }
  ],
  "students": [
    { "id": 101, "name": "Sam", "grade": "10th", "section": "A", "marks": { "math": 85, "science": 90, "english": 88 } },
    { "id": 102, "name": "jaanu", "grade": "10th", "section": "A", "marks": { "math": 92, "science": 87, "english": 91 } },
    { "id": 103, "name": "Ramesh P", "grade": "10th", "section": "B", "marks": { "math": 70, "science": 75, "english": 80 } }
  ]
}
`;

// 1️⃣ Parse JSON string → JavaScript object
const school = JSON.parse(schoolData);
console.log('orginal data',school)
console.log(typeof(school))

console.log("School Name:", school.schoolName);
console.log("Location:", school.location);
console.log("----------------------------------");



// 2️⃣ Convert back to JSON string (stringify)
const jsonString = JSON.stringify(school, null, 2);
console.log("Converted Back to JSON Format:");
console.log(jsonString);
