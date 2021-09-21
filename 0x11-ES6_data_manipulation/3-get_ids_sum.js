export default function getStudentIdsSum(getListStudents) {
  const reducer = (previousValue, currentValue) => previousValue + currentValue.id;
  return getListStudents.reduce(reducer);
}
