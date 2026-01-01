import { useState } from "react";
import { submitTextForSummarization, getTaskStatus } from "../api/summarizer";
import TextInput from "../components/TextInput";
import Loader from "../components/Loader";
import SummaryOutput from "../components/SummaryOutput";

export default function Home() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");

  const pollStatus = async (taskId) => {
    const interval = setInterval(async () => {
      try {
        const result = await getTaskStatus(taskId);
        if (result.status === "SUCCESS") {
          setSummary(result.summary);
          setLoading(false);
          clearInterval(interval);
        }
      } catch (err) {
        setError("कुछ गलत हो गया। कृपया पुन: प्रयास करें।");
        setLoading(false);
        clearInterval(interval);
      }
    }, 2000);
  };

  const handleSubmit = async () => {
    if (text.trim().length < 20) {
      setError("सारांश के लिए कम से कम 20 शब्द आवश्यक हैं।");
      return;
    }
    setError("");
    setSummary("");
    setLoading(true);

    try {
      const taskId = await submitTextForSummarization(text);
      pollStatus(taskId);
    } catch (err) {
      setError("सर्वर से कनेक्ट नहीं हो पाया।");
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        {/* Header Section */}
        <div className="text-center mb-12">
          
          <h1 className="text-4xl md:text-5xl font-extrabold text-slate-900 mb-4 tracking-tight">
            हिंदी टेक्स्ट <span className="text-indigo-600">सारांश</span>
          </h1>
          <p className="text-lg text-slate-600">
            अपने लंबे लेखों को तुरंत संक्षिप्त और सटीक सारांश में बदलें।
          </p>
        </div>

        {/* Main Interface Card */}
        <div className="bg-white rounded-3xl shadow-xl shadow-slate-200/60 border border-slate-100 overflow-hidden">
          <div className="p-6 md:p-8">
            <div className="relative">
              <TextInput 
                value={text} 
                onChange={setText} 
                className="w-full min-h-[250px] p-4 text-lg border-none focus:ring-0 placeholder-slate-400 resize-none"
              />
              
              {/* Character Count/Status Bar */}
              <div className="flex justify-between items-center mt-4 pt-4 border-t border-slate-50">
                <span className="text-sm text-slate-400">
                  {text.length} अक्षर दर्ज किए गए
                </span>
                <button
                  onClick={handleSubmit}
                  disabled={loading}
                  className={`flex items-center gap-2 px-8 py-3 bg-indigo-600 text-white font-bold rounded-xl transition-all shadow-lg shadow-indigo-200 hover:bg-indigo-700 hover:-translate-y-0.5 active:translate-y-0 disabled:opacity-50 disabled:cursor-not-allowed`}
                >
                  {loading ? "प्रक्रिया जारी है..." : "सारांश बनाएँ ✨"}
                </button>
              </div>
            </div>
          </div>

          {/* Feedback Section */}
          {(loading || error || summary) && (
            <div className="bg-slate-50 border-t border-slate-100 p-6 md:p-8">
              {loading && (
                <div className="flex flex-col items-center py-10">
                  <Loader />
                  <p className="mt-4 text-slate-500 animate-pulse">AI आपके टेक्स्ट का विश्लेषण कर रहा है...</p>
                </div>
              )}

              {error && (
                <div className="bg-red-50 border border-red-100 text-red-700 px-4 py-3 rounded-xl flex items-center gap-3">
                  <span>⚠️</span> {error}
                </div>
              )}

              {summary && (
                <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
                  <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">परिणाम</h3>
                  <div className="prose prose-slate max-w-none">
                    <SummaryOutput summary={summary} />
                  </div>
                  <button 
                    onClick={() => navigator.clipboard.writeText(summary)}
                    className="mt-6 text-indigo-600 text-sm font-medium hover:text-indigo-800 flex items-center gap-1"
                  >
                    📋 सारांश कॉपी करें
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer info */}
        <p className="text-center mt-8 text-slate-400 text-sm">
          Project by: Yashraj Jyoti Sanjay Kastode
        </p>
      </div>
    </div>
  );
}