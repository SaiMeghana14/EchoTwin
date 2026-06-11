"use client";

import Link from "next/link";

export default function Sidebar() {
  return (
    <div className="w-64 min-h-screen bg-slate-900 p-5">

      <h2 className="text-2xl font-bold mb-8">
        EchoTwin
      </h2>

      <div className="flex flex-col gap-4">

        <Link href="/dashboard">
          Dashboard
        </Link>

        <Link href="/face-analysis">
          Face Guardian
        </Link>

        <Link href="/voice-analysis">
          Voice Guardian
        </Link>

        <Link href="/writing-analysis">
          Writing Guardian
        </Link>

        <Link href="/threat-center">
          Threat Center
        </Link>

        <Link href="/echovision">
          EchoVision
        </Link>

        <Link href="/twinshield">
          TwinShield
        </Link>

      </div>
    </div>
  );
}
