export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const math = mathFunction();
    queue.push(math);
  } catch (error) {
    queue.push(error.toString());
  }
  queue.push('Guardrail was processed');
  return queue;
}
