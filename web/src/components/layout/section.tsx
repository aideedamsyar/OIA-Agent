import React from 'react';

interface SectionProps {
  title: string;
  subtitle?: string; // Optional subtitle
  children: React.ReactNode;
  className?: string; // Optional additional classes for the section wrapper
}

export function Section({
  title,
  subtitle,
  children,
  className = '',
}: SectionProps) {
  return (
    <section className={`w-full ${className}`}>
      {/* Section Header */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold tracking-wide uppercase text-neutral-800 border-b border-neutral-300 pb-2">
          {title}
        </h2>
        {subtitle && (
          <p className="text-sm text-neutral-600 mt-2">
            {subtitle}
          </p>
        )}
      </div>
      
      {/* Section Content */}
      <div>{children}</div>
    </section>
  );
}

export default Section; 