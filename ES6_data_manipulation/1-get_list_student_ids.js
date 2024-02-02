export default function getListStudentIds(studentArray) {
  // Check if the argument is an array
  if (!Array.isArray(studentArray)) {
    return [];
  }

  // Use the map function to extract student IDs
  const studentIds = studentArray.map((student) => student.id);

  return studentIds;
}
