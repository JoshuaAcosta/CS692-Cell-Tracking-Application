

struct point {
    int row;
    int col;
};
typedef struct point point;

@interface Cell : NSObject {
    BOOL active;
    BOOL tracked;
    int generation;
    int centerRow;
    int centerCol;
    int radius;
    int nLocations;
    int bandLength;
    point * boundary;
}

- (id)initWithNLocations:(int)theNLocations bandLength:(int)theBandLength;

@property(readwrite) BOOL active;
@property(readwrite) BOOL tracked;
@property(readwrite) int generation;
@property(readwrite) int centerRow;
@property(readwrite) int centerCol;
@property(readwrite) int radius;
@property(readwrite) int nLocations;
@property(readwrite, assign) point * boundary;



@synthesize active, tracked, generation, centerRow, centerCol, radius, nLocations, boundary;

- (id)initWithNLocations:(int)theNLocations bandLength:(int)theBandLength
{
    if (self = [super init]) {
        active = NO;
        centerRow = 0;
        centerCol = 0;
        radius = 0;
        nLocations = theNLocations;
        bandLength = theBandLength;
        boundary = (point *)malloc(nLocations*sizeof(point));
    }
    return self;
}


class Cell (self):
    def __init__(self, theNLocations, theBandLength):
        self.theNLocations = theNLocations
        self.stheBandLength = stheBandLength
        active = False
        tracked = False
        generation = 0
        centerRow = 0
        centerCol = 0
        radius = 0
