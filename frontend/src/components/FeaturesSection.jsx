const FeaturesSection = () => {
    const features = [
        { title: 'Trusted Drivers', description: 'All drivers are verified for your safety.' },
        { title: 'Flexible Booking', description: 'Choose trips that match your schedule.' },
        { title: 'Affordable Prices', description: 'Transparent pricing with no hidden fees.' },
    ];

    return (
        <section className="py-16">
            <div className="container mx-auto text-center">
                <h2 className="text-3xl font-bold text-gray-800">Why Choose Us?</h2>
                <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-8">
                    {features.map((feature, index) => (
                        <div key={index} className="shadow-md rounded-md p-6">
                            <h3 className="text-xl font-semibold text-amber-600">{feature.title}</h3>
                            <p className="mt-4 text-gray-600">{feature.description}</p>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default FeaturesSection;