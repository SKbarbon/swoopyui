
import SwiftUI

struct TheListView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        List {
            ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
            }
        }
    }
}
