export default function TextInput({ value, onChange }) {
  return (
    <textarea
      className="w-full h-48 p-4 border rounded-md focus:outline-none focus:ring"
      placeholder="यहाँ हिंदी टेक्स्ट पेस्ट करें..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}
