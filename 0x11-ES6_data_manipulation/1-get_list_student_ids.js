export default function getListStudentIds(newa) {
  if (Array.isArray(newa) === false) {
    return [];
  }

  return newa.map((i) => i.id);
}
