import data from '@/data/notices.json'; // Adjust path as needed
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import Link from 'next/link';
import { format } from 'date-fns'; // Using date-fns for better date formatting
import Hero from '@/components/landing/hero';
import Section from '@/components/layout/section'; // Import the Section component

// Define an interface for the notice structure for type safety
interface Notice {
  title: string;
  link: string;
  date: string;
  passed_language_check?: boolean;
  is_direct_opportunity?: boolean;
  summary?: string | null;
}

export default function Home() {
  const notices: Notice[] = data.notices;
  const lastUpdated = data.last_updated;

  return (
    <>
      <Hero />

      <Section
        title="🔍 Latest Opportunities"
        subtitle="Fresh listings updated daily from university job boards."
      >
        {/* Display Last Updated time within the section */}
        {lastUpdated && (
          <p className="text-xs text-neutral-500 mb-4 text-right">
            Last Updated: {format(new Date(lastUpdated), 'yyyy-MM-dd HH:mm')}
          </p>
        )}
        
        {/* Notice Grid */}
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {notices.length > 0 ? (
            notices.map((notice, index) => (
              <Card key={index} className="bg-white border border-neutral-200 rounded-lg shadow-sm hover:shadow transition-shadow flex flex-col justify-between">
                <CardHeader>
                  <div className="flex justify-between items-start gap-2">
                    <CardTitle className="text-base font-semibold text-neutral-900 leading-snug flex-1">
                      <Link 
                        href={notice.link} 
                        target="_blank" 
                        rel="noopener noreferrer" 
                        className="hover:text-primary hover:underline"
                      >
                        {notice.title}
                      </Link>
                    </CardTitle>
                    {/* Conditionally render Verified Job Badge */}
                    {notice.is_direct_opportunity === true && (
                      <Badge className="bg-success/10 text-success text-xs whitespace-nowrap px-2 py-0.5 rounded-full border border-success/30">
                        Verified Job
                      </Badge>
                    )}
                  </div>
                </CardHeader>
                {/* Conditionally render Summary */}
                {notice.summary && (
                  <CardContent className="py-0 pb-4">
                    <p className="text-sm text-neutral-600 line-clamp-3">
                      {notice.summary}
                    </p>
                  </CardContent>
                )}
                <CardFooter className="flex justify-between items-center text-xs text-neutral-500 mt-auto pt-4">
                  <span>{notice.date}</span>
                  <Link 
                    href={notice.link} 
                    target="_blank" 
                    rel="noopener noreferrer" 
                    className="text-primary hover:underline"
                  >
                    View →
                  </Link>
                </CardFooter>
              </Card>
            ))
          ) : (
            // Use the Empty State style from PRD 7.6
            <div className="text-center py-12 text-neutral-500 md:col-span-2 lg:col-span-3">
              <p>No relevant notices found today. Check back tomorrow.</p>
            </div>
          )}
        </div>
      </Section>
      
      {/* Divider between sections */}
      <div className="border-t border-neutral-300 w-full" />

      <Section 
        title="🎓 Trusted Sources" 
        subtitle="Handpicked from top universities."
      >
        {/* Placeholder Content for Trusted Sources */}
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4 text-center">
          <Card className="p-4 bg-neutral-50 border border-neutral-200 text-sm font-medium text-neutral-600">SNU</Card>
          <Card className="p-4 bg-neutral-50 border border-neutral-200 text-sm font-medium text-neutral-600">POSTECH</Card>
          <Card className="p-4 bg-neutral-50 border border-neutral-200 text-sm font-medium text-neutral-600">Yonsei</Card>
          <Card className="p-4 bg-neutral-50 border border-neutral-200 text-sm font-medium text-neutral-600">Hanyang</Card>
          <Card className="p-4 bg-neutral-50 border border-neutral-200 text-sm font-medium text-neutral-600">More...</Card>
        </div>
      </Section>

      {/* Divider between sections */}
      <div className="border-t border-neutral-300 w-full" />

      <Section 
        title="🤖 Smart Filtering" 
        subtitle="Less noise, more signal. AI helps surface relevant jobs."
      >
        {/* Placeholder Content for Smart Filtering */}
        <Card className="p-6 bg-neutral-50 border border-neutral-200 text-neutral-600">
          <p>Coming soon: AI-powered filtering will analyze notice content to better identify true job opportunities, distinguishing them from info sessions or general announcements.</p>
        </Card>
      </Section>
    </>
  );
}
