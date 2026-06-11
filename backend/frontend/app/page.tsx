import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col justify-center items-center">

      <h1 className="text-6xl font-bold mb-4">
        EchoTwin
      </h1>

      <p className="text-xl text-gray-400 mb-8">
        Your AI Identity Guardian
      </p>

      <div className="flex gap-4">
        <Link
          href="/dashboard"
          className="bg-blue-600 px-6 py-3 rounded-xl"
        >
          Launch Dashboard
        </Link>

        <Link
          href="/face-analysis"
          className="border border-gray-600 px-6 py-3 rounded-xl"
        >
          Analyze Content
        </Link>
      </div>
    </main>
  );
}
