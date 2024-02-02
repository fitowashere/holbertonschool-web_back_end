export default function getStudentIdsSum(studentArray) {
  const idSum = studentArray.reduce((sum, student) => sum + student.id, 0);

  return idSum;
}
