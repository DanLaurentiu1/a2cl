import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import SidePannel from "../ui/dashboard/SidePannel";
import { PlanProvider } from "../context/PlanProvider";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`bg-darkgrey ${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <PlanProvider>
          <div className="flex h-screen">
            <SidePannel />
            <div className="flex-1 p-4">{children}</div>
          </div>
        </PlanProvider>
      </body>
    </html>
  );
}
