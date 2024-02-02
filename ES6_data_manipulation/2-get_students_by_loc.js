export default function getStudentsByLocation(studentArray, location) {
  const studentloc = studentArray.filter((student) => student.location === location);

  return studentloc;
}
