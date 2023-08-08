//
//  TheAnimatedView.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 24/06/2023.
//

import SwiftUI

struct TheAnimatedView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        if textData.resizeable == true {
            VStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
            }
            .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
            .animation(.default, value: UUID())
        }else{
            VStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
            }
            .animation(.default, value: UUID())
        }
    }
}
