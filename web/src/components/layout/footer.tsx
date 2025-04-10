import Link from 'next/link';

export function Footer() {
  return (
    // The top border will be added in the main layout as per the PRD Page Shell example
    <footer className="py-8 text-center">
      <div className="max-w-7xl mx-auto px-6 text-sm text-neutral-500">
        <p className="mb-2">
          Built by students, for students. Opportune is open-source and driven by a
          mission to make opportunity more accessible.
        </p>
        <div className="flex justify-center items-center gap-3">
          {/* External link to GitHub */}
          <a
            href="https://github.com/aideedamsyar/OIA-Agent" // Replace with your actual repo URL if different
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-primary"
          >
            GitHub
          </a>
          <span>·</span>
          {/* Internal links - assuming these pages will exist */}
          <Link href="/privacy" passHref>
            <span className="hover:text-primary cursor-pointer">Privacy</span>
          </Link>
          <span>·</span>
          <Link href="/terms" passHref>
            <span className="hover:text-primary cursor-pointer">Terms</span>
          </Link>
        </div>
      </div>
    </footer>
  );
}

export default Footer; 