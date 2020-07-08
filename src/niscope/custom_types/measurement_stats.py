class MeasurementStats(object):
    def __init__(self, result=0.0, mean=0.0, stdev=0.0, min_val=0.0, max_val=0.0, num_in_stats=0):
        self.result = result
        self.mean = mean
        self.stdev = stdev
        self.min_val = min_val
        self.max_val = max_val
        self.num_in_stats = num_in_stats
        
        self.channel = None
        self.record = None
        
    def __repr__(self):
        parameter_list = [
            'result={}'.format(self.result),
            'mean={}'.format(self.mean),
            'stdev={}'.format(self.stdev),
            'min_val={}'.format(self.min_val),
            'max_val={}'.format(self.max_val),
            'num_in_stats={}'.format(self.num_in_stats)
        ]
        
        return '{0}({1})'.format(self.__class__.__name__, ', '.join(parameter_list))
    
    def __str__(self):
        row_format_g = '{:<20}: {:,.6g}\n'
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'
        
        string_representation = ''
        if self.channel is not None:
            string_representation += row_format_s.format('channel', self.channel)
        if self.record is not None:
            string_representation += row_format_d.format('record', self.record)
            
        string_representation += row_format_g.format('result', self.result)
        string_representation += row_format_g.format('mean', self.mean)
        string_representation += row_format_g.format('standard deviation', self.stdev)
        string_representation += row_format_g.format('minimum value', self.min_val)
        string_representation += row_format_g.format('maximum value', self.max_val)
        string_representation += row_format_d.format('num in stats', self.num_in_stats)
        
        return string_representation
