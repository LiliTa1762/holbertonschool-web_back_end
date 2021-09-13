export default function createIteratorObject(report) {
  const everyEmployee = [];
  for (const k of Object.keys(report.allEmployees)) {
    everyEmployee.push(...report.allEmployees[k]);
  }
  return everyEmployee;
}
