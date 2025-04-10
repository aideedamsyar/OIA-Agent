export function Hero() {
  return (
    <section className="text-center py-16 md:py-24">
      {/* Optional: Add Logo here if desired */}
      {/* <Image src="/logo.svg" alt="Opportune Logo" width={80} height={80} className="mx-auto mb-4" /> */}

      <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-neutral-900">
        Opportune
      </h1>
      <p className="text-lg text-neutral-700 mt-2">
        Right place. Right time.
      </p>
      <p className="mt-4 max-w-2xl mx-auto text-base text-neutral-600">
        Discover curated job and internship opportunities from Korea's top
        universities — all in one place.
      </p>
      {/* Optional: Add a Call to Action button if needed */}
      {/* <Button className="mt-8">View Notices</Button> */}
    </section>
  );
}

export default Hero; 