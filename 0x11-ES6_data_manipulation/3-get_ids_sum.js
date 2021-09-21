export default function getStudentIdsSum(getListStudents) {
  const reducer = getListStudents.reduce((acc, item) => {
    acc += item;
  })
  return reducer;
}
