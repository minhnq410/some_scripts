using App.Metrics;
using App.Metrics.Counter;

namespace TodoAPI
{
    public class MyMetrics
    {
        public static CounterOptions SelfPostCounters => new CounterOptions { 
            Name = "POST Counter",
            Context = "Self-made POST Counter",
            MeasurementUnit = Unit.Calls
        };

        public static CounterOptions SelfGetCounters => new CounterOptions
        {
            Name = "GET Counter",
            Context = "Self-made GET Counter",
            MeasurementUnit = Unit.Calls
        };
    }
}
