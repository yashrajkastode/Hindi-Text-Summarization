export default function SummaryOutput({ summary }) {
  return (
    <div className="mt-6 p-4 bg-gray-100 rounded-md">
      <h2 className="font-semibold mb-2">सारांश</h2>
      <p className="whitespace-pre-wrap">{summary}</p>
    </div>
  );
}
