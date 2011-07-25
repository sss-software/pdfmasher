#import <Cocoa/Cocoa.h>
#import "PyFairware.h"
#import "ProgressController.h"

@interface PyPdfMasher : PyFairware <Worker> {}
- (void)changeStateOfSelected:(NSString *)newstate;
- (void)loadPDF:(NSString *)path;
- (BOOL)hideIgnored;
- (void)setHideIgnored:(BOOL)value;
@end