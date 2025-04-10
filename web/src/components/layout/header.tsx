import Link from 'next/link';

export function Header() {
  return (
    <header className="sticky top-0 z-50 bg-white border-b border-neutral-200 px-6 py-4 flex justify-between items-center">
      {/* Brand Name linked to Home */}
      <Link href="/" passHref>
        <span className="text-xl font-semibold text-primary cursor-pointer">
          Opportune
        </span>
      </Link>
      
      {/* Navigation Links */}
      <nav className="flex gap-6 text-sm text-neutral-700">
        <Link href="/" passHref>
          <span className="hover:text-primary cursor-pointer">Home</span>
        </Link>
        <Link href="/about" passHref>
          <span className="hover:text-primary cursor-pointer">About</span>
        </Link>
        {/* Add other navigation links here if needed */}
      </nav>
    </header>
  );
}

// Exporting as default can sometimes be convenient
export default Header; 