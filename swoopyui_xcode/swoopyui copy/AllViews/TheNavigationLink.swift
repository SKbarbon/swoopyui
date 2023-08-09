import SwiftUI

struct TheNavigationLink: View {
    @State var isNavPresented : Bool = false
    
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        NavigationLink (destination: VStack {
            ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
            }
        }, isActive: $isNavPresented) {
            ForEach(textData.skin_views!, id: \.view_id) { sub_view in
                GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
            }
        }
    }
}
