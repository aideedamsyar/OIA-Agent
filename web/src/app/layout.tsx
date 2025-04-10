import type { Metadata } from "next";
import { IBM_Plex_Sans } from "next/font/google";
import "./globals.css";
import Header from "@/components/layout/header";
import Footer from "@/components/layout/footer";

const ibmPlexSans = IBM_Plex_Sans({
  weight: ['400', '500', '600', '700'],
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-ibm-plex-sans',
});

export const metadata: Metadata = {
  title: "Opportune - Hanyang OIA Notices",
  description: "Curated job and internship notices from Hanyang OIA",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${ibmPlexSans.variable} font-sans`}>
      <body className="min-h-screen bg-background text-neutral-900">
        <Header />
        <main className="max-w-7xl mx-auto px-6 py-12 space-y-16">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
