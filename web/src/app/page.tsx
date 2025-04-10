import data from '@/data/notices.json'; // Adjust path as needed
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import Link from 'next/link';
import { format } from 'date-fns'; // Using date-fns for better date formatting

// Define an interface for the notice structure for type safety
interface Notice {
  title: string;
  link: string;
  date: string;
}

export default function Home() {
  const notices: Notice[] = data.notices;
  const lastUpdated = data.last_updated;

  return (
    <main className="container mx-auto px-4 py-8">
      <div className="mb-6 flex justify-between items-center">
        <h1 className="text-3xl font-bold">Hanyang OIA Notices</h1>
        {lastUpdated && (
          <p className="text-sm text-muted-foreground">
            Last Updated: {format(new Date(lastUpdated), 'yyyy-MM-dd HH:mm:ss')}
          </p>
        )}
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {notices.length > 0 ? (
          notices.map((notice, index) => (
            <Card key={index}>
              <CardHeader>
                <CardTitle className="text-lg leading-tight">
                  <Link href={notice.link} target="_blank" rel="noopener noreferrer" className="hover:underline">
                    {notice.title}
                  </Link>
                </CardTitle>
              </CardHeader>
              <CardFooter>
                <p className="text-sm text-muted-foreground">{notice.date}</p>
              </CardFooter>
            </Card>
          ))
        ) : (
          <p>No relevant notices found.</p>
        )}
      </div>
    </main>
  );
}
