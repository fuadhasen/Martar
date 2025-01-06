const TestimonialsSection = () => {
    const testimonials = [
        { name: 'John Doe', feedback: 'Fantastic service! Highly recommend.' },
        { name: 'Jane Smith', feedback: 'The platform made my trip planning so easy!' },
        { name: 'Ahmed Karim', feedback: 'Reliable and affordable transport options.' },
    ];

    return (
        <section className="bg-gray-100 py-16">
            <div className="container mx-auto text-center">
                <h2 className="text-3xl font-bold text-gray-800">What Our Users Say</h2>
                <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-8">
                    {testimonials.map((testimonial, index) => (
                        <div key={index} className="bg-white shadow-md rounded-md p-6">
                            <p className="text-gray-600">"{testimonial.feedback}"</p>
                            <h3 className="font-semibold text-sm text-amber-800">- {testimonial.name} -</h3>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default TestimonialsSection;