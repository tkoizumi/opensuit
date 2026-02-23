import { Button } from "@/components/ui/button";
import { Slack } from "lucide-react";

export default function App() {
  const handleSlackIntegration = () => {
    alert("Slack integration would be initiated here.");
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-10 bg-gray-50">
      <div className="max-w-2xl w-full text-center">
        {/* Header */}
        <div className="mb-12">
          <h1 className="text-5xl font-bold text-gray-900 mb-6">OpenSuit</h1>
          <p className="text-xl text-gray-600 max-w-lg mx-auto">
            An open-source AI assistant platform that integrates seamlessly with
            your existing tools.
          </p>
        </div>

        {/* Slack Integration Card */}
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-md mx-auto border border-gray-200">
          <div className="flex flex-col items-center">
            <div className="w-16 h-16 bg-[#4A154B] rounded-xl flex items-center justify-center mb-6">
              <Slack className="w-8 h-8 text-white" />
            </div>

            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Integrate with Slack
            </h2>

            <p className="text-gray-600 mb-8">
              Add OpenSuit to your Slack workspace to get AI-powered assistance
              directly in your channels.
            </p>

            <Button
              onClick={handleSlackIntegration}
              className="bg-[#4A154B] hover:bg-[#3a0f3a] text-white px-8 py-6 text-lg w-full"
              size="lg"
            >
              <Slack className="w-5 h-5 mr-2" />
              Add to Slack
            </Button>
          </div>
        </div>

        {/* Footer */}
        <footer className="mt-12 pt-8 border-t border-gray-200">
          <p className="text-gray-500">
            © {new Date().getFullYear()} OpenSuit. Open source AI assistant
            platform.
          </p>
        </footer>
      </div>
    </div>
  );
}
